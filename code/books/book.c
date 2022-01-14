class BookFilter{
    virtual bool apply(Book) = 0;
};
class TitleFilter : public BookFilter{
    private: std::string m_title;
    public: TitleFilter(std::string title)
    {
        m_title = title;
       }
    override bool apply(const Book& book)
    {

        if (Book.title.find(m_title) != std::string::npos)
        return true;

    return false
    }
};


typedef enum{
Big,
Medium,
Small
} BookSize;


class BookSizeFilter : BookFilter{
    private: BookSizeFilter(BookSize desiredSize){
    m_desiredSize = desiredSize;
    }
    override bool apply(const Book& book){
        unsigned int minPages = 0;
        unsignedint maxPages = 0;

        switch m_desiredSize{
            case Big:
                minPages = 0;
                maxPages = 100;
            case Medium:
                minPages = 101;
                maxPages = 500;
            case Small:
                minPages = 501;
                maxPages = std::UINT_MAX;
        }
    return (Book.pageCount >= minPages) && (Book.pageCount < maxPages);
    }
}

bool BookPassesFilters(const Book& book, std::List<BookFilter>& filters){
    for (BookFilter filter : filters){
        if (!filter.apply(book))
            return false;
    }
    return true;
    }

    std::set<Book> FilterBooks(std::List<Book> bookList, std::List<BookFilter>& filters){
    std::set<Book> rval;
    for (Book book : bookList){
        if (bookPassesFilters(book, filters))
            rval.push_back(book);
    }
    return rval;
}
